package org.kirish.candyservice.exceptions;

public class CandyNotFoundException extends RuntimeException {
    public CandyNotFoundException(String message) {
        super(message);
    }
}
