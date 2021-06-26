package org.kirish.candyservice.exceptions;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value = HttpStatus.NOT_FOUND, reason = "Candy was not found")
public class CandyNotFoundException extends RuntimeException {
    public CandyNotFoundException(String message) {
        super(message);
    }
}
