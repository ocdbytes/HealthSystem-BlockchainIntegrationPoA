import express from "express";
import config from 'config';
import log from "./utils/logger";
import connect from "./DB/connect";
import routes from "./routes";
import { deserializeUser } from "./middleware/deserializeUser";

const port = config.get<number>("port");
const host = config.get<string>("host");

const app = express();
app.use(express.json());
app.use(deserializeUser);

app.listen(port,host, () => {
    log.info(`Server listening at http://${host}:${port}`);
    connect();
    routes(app);
})