package org.kirish.candyservice.service;

import org.kirish.candyservice.domain.Candy;
import org.kirish.candyservice.exceptions.CandyNotFoundException;
import org.kirish.candyservice.jpa.CandyRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class CandyService {

    private static final Logger LOGGER = LoggerFactory.getLogger(CandyService.class);

    @Autowired
    private CandyRepository candyRepository;

    /**
     * Saves candy in DB by given Candy object.
     * @param candyToSave candy that is going to be saved in DB.
     * @return candy's ID as long from DB.
     */
    public long saveCandyInDB(Candy candyToSave) {
        return candyRepository.save(candyToSave).getId();
    }

    /**
     * Updates a candy in DB by given Candy object. In case candy was not found in DB by
     * given candyId the CandyNotFoundException is thrown.
     * @param candyToUpdate candy that is going to be a new one. ID has to be the same
     *                      as the same one in repository.
     * @return candy's ID as long from DB.
     */
    public long updateCandyInDB(Candy candyToUpdate) {
        Candy candy = candyRepository
                .findById(candyToUpdate.getId())
                .orElseThrow(() -> new CandyNotFoundException(
                        String.format("Candy with id %s was not found", candyToUpdate.getId())
                ));
        candy.setName(candyToUpdate.getName());
        return candyRepository.save(candy).getId();
    }

    /**
     * Retrieves a single candy from DB by given ID.
     * @param id id of candy to be retrieved.
     * @return instance of Candy.
     */
    public Candy getCandyByIdFromDB(long id) {
        return candyRepository.findById(id).orElseThrow(() -> new CandyNotFoundException(
                String.format("Candy with id %s was not found", id)
        ));
    }

    /**
     * Retrieves all candies from DB.
     * @return Iterable of Candy.
     */
    public Iterable<Candy> getAllCandies() {
        return candyRepository.findAll();
    }

    /**
     * Deletes a candy in DB by given ID.
     * @param id id of candy to be deleted.
     */
    public void deleteCandyById(long id) {
        //Doing deletion via retrieving Candy from DB in order to check if Candy exists
        Candy candyToDelete = this.getCandyByIdFromDB(id);
        candyRepository.deleteById(candyToDelete.getId());
    }

}
