package com.example.springcalculator.component;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;

@SpringBootTest
public class DollarCalTest {

    @MockBean
    private MarketApi marketApi;

    @Autowired
    private Cal cal;

    @Test
    public void dct(){
        Mockito.when(marketApi.connect()).thenReturn(3000);

        int sum = cal.sum(10, 10);
        int minus = cal.minus(10, 10);
        Assertions.assertEquals(60000, sum);
    }
}
