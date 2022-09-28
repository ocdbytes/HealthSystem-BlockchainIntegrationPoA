import * as dotenv from 'dotenv';
dotenv.config();

export default {
    host : process.env.HOST ?? '',
    environment : process.env.NODE_ENV ?? '',
    port : process.env.PORT ?? '',
    dbURI : process.env.DB_URI ?? '',
    dbName : process.env.DB_NAME ?? '',
    corsUrl : process.env.CORS_URL ?? '',
    ACCESS_TOKEN_PRIVATE_KEY : process.env.ACCESS_TOKEN_PRIVATE_KEY ?? '',
    ACCESS_TOKEN_PUBLIC_KEY : process.env.ACCESS_TOKEN_PUBLIC_KEY ?? '',
    REFRESH_TOKEN_PRIVATE_KEY : process.env.REFRESH_TOKEN_PRIVATE_KEY ?? '',
    REFRESH_TOKEN_PUBLIC_KEY : process.env.REFRESH_TOKEN_PUBLIC_KEY ?? '',
    accessTokenTtl : '60m',
    refreshTokenTtl : '1y'
}