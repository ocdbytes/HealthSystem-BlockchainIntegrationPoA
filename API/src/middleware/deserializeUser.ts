import {Request,Response,NextFunction} from 'express';
import {get} from 'lodash'
import { reIssueAccessToken } from '../service/session.service';
import { verifyJwt } from '../utils/jwt.utils';

// this middleware is to get the user data and authenticate the user's tokens upon when every request is being made
export const deserializeUser = async(req:Request,res:Response,next:NextFunction) => {
    // To print the request
    // console.log(req.headers);

    const accessToken = get(req, "headers.authorization", "").replace(/^Bearer\s/,"");
    const refreshToken = get(req, "headers.x-refresh");

    // If access token is not there we will forward our function to the next
    if(!accessToken) return next();
    // First we will verify the refresh token
    const {decoded,expired} = verifyJwt(accessToken,"accessPublicKey");

    // If decoded returned is not null
    if(decoded){
        res.locals.user = decoded;
        return next();
    }

    if(expired && refreshToken){
        // getting the new access token
        const newAccessToken = await reIssueAccessToken({refreshToken});
        if(newAccessToken){
            // setting the access token in response header
            res.setHeader('x-access-token',newAccessToken);
        }
        // verify the newly generated token in order to get the user
        const result  = verifyJwt(newAccessToken.toString(),"accessPublicKey");
        // Setting the locals.user as the results.decoded
        res.locals.user = result.decoded;
        return next();
    }

    return next();
}
