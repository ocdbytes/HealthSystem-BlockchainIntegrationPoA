import mongoose from "mongoose";
import bcrypt from "bcrypt";
import config from "config";

export interface UserInput {
    email : string;
    name  :string;
    password : string;
}

export interface UserDocument extends UserInput, mongoose.Document{
    createdAt : Date;
    updatedAt : Date;
    comparePassword(candidatePassword : string) : Promise<Boolean>
}

const UserSchema = new mongoose.Schema(
    {
        email : {type:String, required : true, unique : true},
        name : {type : String, required: true},
        password : {type: String, required : true}
    },
    {
        timestamps :true
    }
);

UserSchema.pre("save", async function (next){
    let user = this as UserDocument;
    console.log(user);

    if(!user.isModified("password")){
        return next();
    }

    const salt = await bcrypt.genSalt(config.get<number>("saltworkfactor"));

    const hash = await bcrypt.hashSync(user.password, salt);

    user.password = hash;
    return next();
})

UserSchema.methods.comparePassword = async function(
    candidatePassword : string
):Promise<boolean>{
    const user  = this as UserDocument;
    return bcrypt.compare(candidatePassword, user.password).catch((e) => false);
}

const UserModel = mongoose.model<UserDocument>('User', UserSchema);

export default UserModel;