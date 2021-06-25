package org.kirish.candyservice.jpa;

import org.kirish.candyservice.domain.Candy;
import org.springframework.data.repository.CrudRepository;

public interface CandyRepository extends CrudRepository<Candy, Long> {
}
