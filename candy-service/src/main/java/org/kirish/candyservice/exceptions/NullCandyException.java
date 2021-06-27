package org.kirish.candyservice.exceptions;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value = HttpStatus.BAD_REQUEST, reason = "Candy cannot be null!")
public class NullCandyException extends RuntimeException {
    public NullCandyException(String message) {
        super(message);
    }

    public NullCandyException(String message, Throwable throwable) {
        super(message, throwable);
    }

    public NullCandyException(Throwable throwable) {
        super(throwable);
    }
}
