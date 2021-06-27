package org.kirish.candyservice.web;

import org.kirish.candyservice.domain.Candy;
import org.kirish.candyservice.domain.ErrorMessage;
import org.kirish.candyservice.domain.ResponseMessage;
import org.kirish.candyservice.exceptions.CandyNotFoundException;
import org.kirish.candyservice.exceptions.NullCandyException;
import org.kirish.candyservice.jpa.CandyRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.Objects;

@RestController
@RequestMapping(path = "/candy")
public class CandyController {

    Logger logger = LoggerFactory.getLogger(CandyController.class);

    @Autowired
    private CandyRepository candyRepository;

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
        logger.info("Receiving new request for creating candy: " + candyToCreate.toString());
        long id = candyRepository.save(candyToCreate).getId();
        return new ResponseMessage(id, "Candy has been created.");
    }

    @PutMapping
    public ResponseMessage updateCandy(@RequestBody Candy candyToUpdate) {
        Candy candy = candyRepository
                .findById(candyToUpdate.getId())
                .orElseThrow(() -> new CandyNotFoundException(
                        String.format("Candy with id %s was not found", candyToUpdate.getId())
                ));
        candy.setName(candyToUpdate.getName());
        candyRepository.save(candy);
        return new ResponseMessage(candy.getId(), "Candy has been updated.");
    }

    @DeleteMapping("/{id}")
    public ResponseMessage deleteCandy(@PathVariable long id) {
        candyRepository.deleteById(id);
        return new ResponseMessage(id, "Candy has been deleted");
    }

    @GetMapping("/{id}")
    public Candy getSingleCandyById(@PathVariable long id) {
        return candyRepository.findById(id).orElseThrow(() -> new CandyNotFoundException(
                String.format("Candy with id %s was not found", id)
        ));
    }

    @GetMapping("/all")
    public Iterable<Candy> getAllCandies() {
        logger.info("Receiving new request for getting all persons");
        return candyRepository.findAll();
    }

}
