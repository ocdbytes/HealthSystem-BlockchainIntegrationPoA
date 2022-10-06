import {Request,Response} from 'express';
import Logger from '../../core/Logger';
import { CreateUserInput } from '../schema/user.schema';
import { createUser } from '../service/user.service';


export async function createUserHandler(req:Request<{},{},CreateUserInput["body"]>, res: Response){
    try {
        //@ts-ignore
        const user = await createUser(req.body);
        return res.send(user);
    } catch (e:any) {
         Logger.error(e);
        return res.status(409).send(e.message);
    }
}