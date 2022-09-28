import SessionModel, { SessionDocument } from "../model/session.model";
import {FilterQuery,UpdateQuery} from 'mongoose'
import { signJwt, verifyJwt } from "../utils/jwt.utils";
import {get} from "lodash";
import config from 'config';
import { findUser } from "./user.service";

export async function createSession(userId : string, userAgent : string){
    const session = await SessionModel.create({user : userId, userAgent});
    return session.toJSON();
}

export async function findSessions(query: FilterQuery<SessionDocument>){
    return SessionModel.find(query).lean();
}

export async function updateSession(query: FilterQuery<SessionDocument>, update: UpdateQuery<SessionDocument>){
    return SessionModel.updateOne(query,update);
}

export async function reIssueAccessToken({refreshToken}:{refreshToken : string}){
    // getting the decoded object from verifyJwt object
    const {decoded} = await verifyJwt(refreshToken,"refreshPublicKey");
    // if !decoded or decoded is not returned
    if(!decoded || !get(decoded, "")) return false;
    // getting the session
    const session = await SessionModel.findById(get(decoded, "session"));
    // checking if session is valid or not
    if(!session || !session.valid) return false;
    //getting the user
    const user = await findUser({_id: session.user});
    // if user is not returned
    if(!user) return false;
    // if valid user is returned
    const accessToken = signJwt({...user, session : session._id},    "accessPrivateKey",{expiresIn : config.get("accessTokenTtl")});

    return accessToken;
}