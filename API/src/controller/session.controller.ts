import {Request,Response} from 'express';
import { createSession, findSessions, updateSession } from '../service/session.service';
import { validatePassword } from '../service/user.service';
import { signJwt } from '../utils/jwt.utils';
import config from 'config'

export async function createUserSessionHandler(req:Request, res:Response){
    // Steps to follow to create a session : 
    // * Validate the User's Password
    // * create a session
    // * create an access token
    // * create an refresh token
    // * return access and refresh token

    const user = await validatePassword(req.body);

    if(!user){
        res.status(401).send("Invalid Credentials")
    }else{
        const session = await createSession(user._id, req.get("userAgent") || "");

        // Now we need a middleware to sign and verify our tokens so we will make that

        const accessToken = signJwt({...user, session: session._id} ,"accessPrivateKey",{expiresIn: config.get("accessTokenTtl")})

        const refreshToken = signJwt({...user, session: session._id} ,"refreshPrivateKey",{expiresIn: config.get("refreshTokenTtl")})

        return res.send({accessToken, refreshToken});
    }
}

export async function getUserSessionsHandler(req:Request, res:Response){
    const userId = res.locals.user._id;
    const sessions = await findSessions({user:userId,valid:true});
    res.send(sessions);
}

export async function deleteSessionsHandler(req:Request, res:Response){
    const sessionId = res.locals.user.session;
    await updateSession({_id: sessionId},{valid: false});
    return res.send({
        accessToken : null,
        refreshToken: null
    })
}