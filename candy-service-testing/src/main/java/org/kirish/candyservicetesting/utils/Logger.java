package org.kirish.candyservicetesting.utils;

import org.apache.logging.log4j.LogManager;
import org.springframework.stereotype.Component;

@Component
public class Logger {

    private static final org.apache.logging.log4j.Logger LOGGER = LogManager.getLogger(Logger.class);

    public void info(String message, Object... args) {
        LOGGER.info(message, args);
    }

}
