package org.kirish.candyservice.controllers;

import org.kirish.candyservice.domain.ErrorMessage;
import org.kirish.candyservice.exceptions.CandyNotFoundException;
import org.kirish.candyservice.exceptions.NullCandyException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

@ControllerAdvice
public class CandyServiceExceptionHandler extends ResponseEntityExceptionHandler {

    @ExceptionHandler({CandyNotFoundException.class, NullCandyException.class})
    private ResponseEntity<Object> handleNotFoundException(RuntimeException ex) {
        HttpStatus httpStatusToReturn;
        if (CandyNotFoundException.class.equals(ex.getClass())) {
            httpStatusToReturn = HttpStatus.NOT_FOUND;
        } else if (NullCandyException.class.equals(ex.getClass())) {
            httpStatusToReturn = HttpStatus.BAD_REQUEST;
        } else {
            httpStatusToReturn = HttpStatus.INTERNAL_SERVER_ERROR;
        }
        return new ResponseEntity<>(new ErrorMessage(ex.getClass().getName(), ex.getMessage()), httpStatusToReturn);
    }

}
