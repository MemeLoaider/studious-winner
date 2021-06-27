package org.kirish.candyservicetesting.configuration;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@ComponentScan("org.kirish.candyservicetesting")
@PropertySource("classpath:application.properties")
public class TestingFrameworkConfiguration {
}
