package org.kirish.candyservice.web;

import org.kirish.candyservice.domain.Candy;
import org.kirish.candyservice.domain.ResponseMessage;
import org.kirish.candyservice.exceptions.CandyNotFoundException;
import org.kirish.candyservice.jpa.CandyRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping(path="/candy")
public class CandyController {

    Logger logger = LoggerFactory.getLogger(CandyController.class);

    @Autowired
    private CandyRepository candyRepository;

    @PostMapping
    public ResponseMessage createCandy(@RequestBody Candy candyToCreate) {
        logger.info("Receiving new request for creating person: " + candyToCreate.toString());
        long id = candyRepository.save(candyToCreate).getId();
        return new ResponseMessage(id, "Candy has been created.");
    }

    @PutMapping
    public ResponseMessage updateCandy(@RequestBody Candy candyToUpdate) {
        Candy candy = null;
        try {
            candy = candyRepository
                    .findById(candyToUpdate.getId())
                    .orElseThrow(() -> new CandyNotFoundException(
                            String.format("Candy with id %s was not found", candyToUpdate.getId())
                    ));
        } catch (CandyNotFoundException exception) {
            return new ResponseMessage(candyToUpdate.getId(), exception.getMessage());
        }
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
