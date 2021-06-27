package org.kirish.candyservice.web;

import org.kirish.candyservice.domain.Candy;
import org.kirish.candyservice.domain.ErrorMessage;
import org.kirish.candyservice.domain.ResponseMessage;
import org.kirish.candyservice.exceptions.CandyNotFoundException;
import org.kirish.candyservice.exceptions.NullCandyException;
import org.kirish.candyservice.service.CandyService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.Objects;

@RestController
@RequestMapping(path = "/candy")
public class CandyController {

    private static final Logger LOGGER = LoggerFactory.getLogger(CandyController.class);

    @Autowired
    private CandyService candyService;

    @ResponseStatus(HttpStatus.NOT_FOUND)
    @ExceptionHandler(CandyNotFoundException.class)
    private ErrorMessage handleNotFoundException(HttpServletRequest request, Exception ex) {
        return new ErrorMessage(request.getRequestURI(), ex.getMessage());
    }

    @PostMapping
    public ResponseMessage createCandy(@RequestBody Candy candyToCreate) {
        if(Objects.isNull(candyToCreate)) {
            throw new NullCandyException("In order to create a candy it has to be not null!");
        }
        LOGGER.info("Receiving new request for creating candy: " + candyToCreate.toString());
        long id = candyService.saveCandyInDB(candyToCreate);
        return new ResponseMessage(id, "Candy has been created.");
    }

    @PutMapping
    public ResponseMessage updateCandy(@RequestBody Candy candyToUpdate) {
        LOGGER.info(String.format("Receiving new request for updating candy with ID: %s", candyToUpdate.getId()));
        long candyId = candyService.updateCandyInDB(candyToUpdate);
        return new ResponseMessage(candyId, "Candy has been updated.");
    }

    @DeleteMapping("/{id}")
    public ResponseMessage deleteCandy(@PathVariable long id) {
        LOGGER.info(String.format("Receiving new request for deleting candy by ID: %s", id));
        candyService.deleteCandyById(id);
        return new ResponseMessage(id, "Candy has been deleted");
    }

    @GetMapping("/{id}")
    public Candy getSingleCandyById(@PathVariable long id) {
        LOGGER.info(String.format("Receiving new request for getting single candy by ID: %s", id));
        return candyService.getCandyByIdFromDB(id);
    }

    @GetMapping("/all")
    public Iterable<Candy> getAllCandies() {
        LOGGER.info("Receiving new request for getting all persons");
        return candyService.getAllCandies();
    }

}
