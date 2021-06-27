package org.kirish.candyservicetesting;

import org.kirish.candyservicetesting.configuration.TestingFrameworkConfiguration;
import org.kirish.candyservicetesting.utils.Logger;
import org.kirish.candyservicetesting.web.CandyService;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class BaseTest {

    public static final AnnotationConfigApplicationContext CONTEXT =
            new AnnotationConfigApplicationContext(TestingFrameworkConfiguration.class);

    protected Logger LOGGER = CONTEXT.getBean(Logger.class);
    protected CandyService CANDY_SERVICE = CONTEXT.getBean(CandyService.class);

}
