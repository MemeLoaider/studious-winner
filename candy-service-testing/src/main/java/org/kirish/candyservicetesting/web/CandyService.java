package org.kirish.candyservicetesting.web;

import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import lombok.Data;
import org.kirish.candyservicetesting.dto.Candy;
import org.kirish.candyservicetesting.dto.DataTransferObject;
import org.kirish.candyservicetesting.utils.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
@Data
public class CandyService {

    private static final String GET_SINGLE_CANDY = "/candy/";

//    @AllArgsConstructor
//    @Getter
//    private enum CandyServiceEndpoints {
//        GET_SINGLE_CANDY("/candy/%s");
//        private final String value;
//    }

    private final String baseUri;
    private final Logger logger;
    private final RequestSpecification requestSpecification;

    @Autowired
    public CandyService(@Value("${candyservice.baseuri}") String baseUri, Logger logger) {
        this.baseUri = baseUri;
        this.logger = logger;
        this.requestSpecification = new RequestSpecBuilder()
                .setBaseUri(this.baseUri).setAccept(ContentType.JSON).build();
    }

    public Candy getSingleCandyByID(String id) {
        logger.info("Sending request to get single candy with following ID: {}", id);
        Response response = RestAssured.given(this.requestSpecification)
                .get(GET_SINGLE_CANDY + id);
        return DataTransferObject.fromJson(response.getBody().jsonPath().prettify(), Candy.class);
    }

}
