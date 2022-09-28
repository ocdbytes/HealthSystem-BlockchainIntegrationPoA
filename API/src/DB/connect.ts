import mongoose from "mongoose";
import config from 'config';
import log from "../utils/logger";

const connect = () => {
    const dbURI = config.get<string>("dbURI");
    return mongoose.connect(dbURI).then(()=>{
        log.info("Database Connected!!")
    }).catch((err)=>{
        log.error("dberror", err);
        process.exit(1);
    })
}

export default connect;