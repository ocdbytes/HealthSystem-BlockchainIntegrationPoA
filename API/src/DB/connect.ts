import mongoose from "mongoose";
import config from 'config';
import Logger from "../../core/Logger";


const connect = () => {
    const dbURI = config.get<string>("dbURI");
    return mongoose.connect(dbURI).then(()=>{
        Logger.info("Database Connected!!")
    }).catch((err)=>{
        Logger.error("dberror", err);
        process.exit(1);
    })
}

export default connect;