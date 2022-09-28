import { Express,Request, Response} from "express";
import { createUserSessionHandler, deleteSessionsHandler, getUserSessionsHandler } from "./controller/session.controller";
import { createUserHandler } from "./controller/user.controller";
import requireUser from "./middleware/requireUser";
import validate from "./middleware/validateResources";
import { createSessionSchema } from "./schema/session.schema";
import { createUserSchema } from "./schema/user.schema";

export default function (app: Express) {
    app.get("/healthCheck",(req:Request, res:Response) => {
        res.sendStatus(200);
    })

    // USER ROUTES
    //------------

    // Register User
    app.post('/api/register', validate(createUserSchema), createUserHandler);
    // Login User
    app.post('/api/sessions', validate(createSessionSchema), createUserSessionHandler);
    // Get User Sessions
    app.get('/api/sessions',requireUser,getUserSessionsHandler);
    // Delete User Sessions
    app.delete('/api/sessions', requireUser, deleteSessionsHandler);

}