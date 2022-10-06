import winston from "winston";

const Logger = winston.createLogger({
  transports: [
    new winston.transports.Console({
      level: "debug",
      handleExceptions: true,
      format: winston.format.combine(
        winston.format.timestamp({ format: "HH:mm:ss:ms" }),
        winston.format.colorize(),
        winston.format.printf(
          (info) => `${info.timestamp} ${info.level}: ${info.message}`
        )
      ),
    }),
  ],
  exitOnError: false,
});
winston.addColors({
  error: "red",
  warn: "yellow",
  info: "cyan",
  debug: "green",
  http: "blue",
});

if (process.env.NODE_ENV === "dev") {
  Logger.add(
    new winston.transports.File({
      level: "info",
      filename: "./logs/all-logs.log",
      handleExceptions: true,
      format: winston.format.combine(
        winston.format.timestamp({
          format: "YYYY-MM-DD HH:mm:ss",
        }),
        winston.format.errors({ stack: true }),
        winston.format.printf(
          (info) => `${info.timestamp} ${info.level}: ${info.message}`
        )
        // winston.format.splat(),
        // winston.format.json()
      ),
      maxsize: 5242880, //5MB
      maxFiles: 5,
    })
  );
}
Logger.info("logging started");

export default Logger;