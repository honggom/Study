package com.example.jpapractice.repository;

import com.example.jpapractice.dto.Gender;
import com.example.jpapractice.dto.User;
import org.assertj.core.util.Lists;
import org.hibernate.criterion.Order;
import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.*;
import java.util.ArrayList;
import java.util.List;

import static org.springframework.data.domain.ExampleMatcher.GenericPropertyMatchers.endsWith;
import static org.springframework.data.domain.ExampleMatcher.GenericPropertyMatchers.startsWith;

@SpringBootTest
class UserRepositoryTest {

    private final Logger logger = LoggerFactory.getLogger(this.getClass());

    @Autowired
    private UserRepository userRepository;


    @Test
    void crud() {
        userRepository.findAll().forEach(user -> {
            logger.info("user : "+user);
        });
    }

    @Test
    void crud2() {
        List<User> users = userRepository.findAll(Sort.by(Sort.Direction.DESC, "name"));
        users.forEach(user -> {
            logger.info("user : "+user);
        });
    }

    @Test
    void crud3() {
        List<User> users = userRepository.findAllById(Lists.newArrayList(1L, 3L, 5L));
        users.forEach(user -> {
            logger.info("user : "+user);
        });
    }

    @Test
    void crud4() {
        User user1 = new User("jack", "jack@naver.com");
        User user2 = new User("steve", "steve@naver.com");

        userRepository.saveAll(Lists.newArrayList(user1, user2));
        List<User> users = userRepository.findAll();
        users.forEach(user -> {
            logger.info("user : "+user);
        });
    }

    @Test
    void crud5() {
        User user = userRepository.findById(1L).orElse(null);
        logger.info("user : "+user);
    }

    @Test
    void crud6() {
        userRepository.saveAndFlush(new User("newHong", "newHong@naver.com"));
        userRepository.findAll().forEach(user -> {
            logger.info("user : "+user);
        });
    }

    @Test
    void crud7() {
        long count = userRepository.count();

        logger.info("count---------");
        logger.info("count : "+count);
        logger.info("count---------");
    }

    @Test
    void crud8() {
        boolean exists = userRepository.existsById(1L);

        logger.info("exists");
        logger.info("exists : "+exists);
        logger.info("exists");
    }

    @Test
    void crud9() {
        userRepository.delete(userRepository.findById(1L).orElseThrow(RuntimeException::new));
    }

    @Test
    void crud10() {
        userRepository.deleteById(1L);
        userRepository.findAll().forEach(user -> {
            logger.info("user : "+user);
        });
    }

    @Test
    void crud11() {
        userRepository.deleteAll();
        userRepository.findAll().forEach(user -> {
            logger.info("user : "+user);
        });
    }

    @Test
    void crud12() {
        // 이 로직에서 select 3번 실행됨
        // findAllById 한 번
        // deleteAll 각 한 번씩 두 번
        // 따라서 비효울적임
        userRepository.deleteAll(userRepository.findAllById(Lists.newArrayList(1L, 3L)));
        userRepository.findAll().forEach(user -> {
            logger.info("user : "+user);
        });
    }

    @Test
    void crud13() {
        // 이 로직은 crud12와 같은 결과지만 select가 2번 실행됨
        // findAllById 한 번
        // deleteInBatch 한 번
        userRepository.deleteInBatch(userRepository.findAllById(Lists.newArrayList(1L, 3L)));
        userRepository.findAll().forEach(user -> {
            logger.info("user : "+user);
        });
    }

    @Test
    void crud14() {
        // 모든 데이터를 지울 경우
        // deleteAllInBatch는 한 번에 쿼리로 다 지움
        userRepository.deleteAllInBatch();
        userRepository.findAll().forEach(user -> {
            logger.info("user : "+user);
        });
    }

    @Test
    void crud15() {
        Page<User> users = userRepository.findAll(PageRequest.of(0, 3));

        logger.info("page : "+users);
        logger.info("totalElements : "+users.getTotalElements());
        logger.info("totalPages : "+users.getTotalPages());
        logger.info("numberOfElements : "+users.getNumberOfElements());
        logger.info("sort : "+users.getSort());
        logger.info("size : "+users.getSize());

        users.forEach(user -> {
            logger.info("user : "+user);
        });
    }

    @Test
    void crud16() {
        ExampleMatcher matcher = ExampleMatcher.matching()
                .withIgnorePaths("name")
                .withMatcher("email", endsWith());

        Example<User> example = Example.of(new User("mo", "mo@nvaer.com"), matcher);

        userRepository.findAll(example).forEach(
                user -> {
                    logger.info("user : "+user);
                }
        );
    }

    @Test
    void crud17() {
        userRepository.save(new User("bong", "bong@naver.com"));

        User user = userRepository.findById(1L).orElseThrow(RuntimeException::new);
        user.setEmail("changed@naver.com");

        userRepository.save(user);

        List<User> users = userRepository.findAll();
        users.forEach(
                u -> {
                    logger.info("user : "+u);
                }
        );
    }

    @Test
    void crud18() {
        logger.info("user : "+userRepository.findByName("aaa"));
    }

    @Test
    void crud19() {
        //메서드 네이밍으로 JPA가 알아서 쿼리 생성 및 실행
        //전부 같은 로직으로 동작
        logger.info("findByEmail : "+userRepository.findByEmail("hong@naver.com"));
        logger.info("getByEmail : "+userRepository.getByEmail("hong@naver.com"));
        logger.info("readByEmail : "+userRepository.readByEmail("hong@naver.com"));
        logger.info("queryByEmail : "+userRepository.queryByEmail("hong@naver.com"));
        logger.info("searchByEmail : "+userRepository.searchByEmail("hong@naver.com"));
        logger.info("streamByEmail : "+userRepository.streamByEmail("hong@naver.com"));
        logger.info("findUserByEmail : "+userRepository.findUserByEmail("hong@naver.com"));
    }

    @Test
    void crud20() {
        logger.info("something : "+userRepository.findSomethingByEmail("hong@naver.com"));
    }

    @Test
    void crud21() {
        logger.info("findByEmailAndName : "+userRepository.findByEmailAndName("hong@naver.com", "hong"));
    }

    @Test
    void crud22() {
        logger.info("findByNameStartingWith : "+userRepository.findByNameStartingWith("ho"));
        logger.info("findByNameEndingWith : "+userRepository.findByNameEndingWith("d"));
        logger.info("findByNameContains : "+userRepository.findByNameContains("o"));
    }

    @Test
    void crud23() {
        logger.info("findByNameLike : "+userRepository.findByNameLike("o"));
        logger.info("findByNameLike : "+userRepository.findByNameLike("%o%"));
    }

    @Test
    void crud24() {
        logger.info("findTop1ByName : "+userRepository.findTop1ByName("hong"));
    }

    @Test
    void crud25() {
        logger.info("findLast1ByName : "+userRepository.findLast1ByName("hong"));
    }

    @Test
    void paging() {
        logger.info("findByName : "+userRepository.findByName("hong", PageRequest.of(0, 1, Sort.by(Sort.Order.desc("id")))).getContent());
    }

    @Test
    void insertAndUpdateTest() {
        //User의
        //@Column(updatable = false)
        //@Column(insertable = false)
        //test
        User user = new User();
        user.setName("hong");
        user.setEmail("hong@naver.com");

        userRepository.save(user);

        User user2 = userRepository.findById(1L).orElseThrow(RuntimeException::new);
        user2.setName("hoooooooooong");

        userRepository.save(user2);
    }

    @Test
    void enumTest() {
        User user = userRepository.findById(1L).orElseThrow(RuntimeException::new);
        user.setGender(Gender.MALE);

        userRepository.save(user);

        userRepository.findAll().forEach(
                u -> {
                    logger.info("user : "+u);
                }
        );
        logger.info("Map : "+userRepository.findRowRecord().get("name"));
        logger.info("Native Query : "+userRepository.findRowRecord().get("gender"));
    }
}














































