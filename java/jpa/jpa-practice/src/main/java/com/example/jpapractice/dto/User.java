package com.example.jpapractice.dto;

import lombok.*;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import javax.persistence.*;
import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
@EqualsAndHashCode
@Builder
@Entity
@EntityListeners(value = {AuditingEntityListener.class, UserEntityListener.class})
@Table(name = "user")
public class User implements Auditable{

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) //생성 방법을 db에 맡기겠다.
    private Long id;

    @NonNull
    private String name;

    @NonNull
    private String email;

    @Enumerated(value = EnumType.STRING)
    private Gender gender;

    @Column(updatable = false)
    private LocalDateTime createdAt;

    @Column(insertable = false)
    private LocalDateTime updatedAt;

    @Transient
    private String testData;

    @PrePersist
    public void prePersist() {
        System.out.println(">>> prePersist");
    }

    @PostPersist
    public void postPersist() {
        System.out.println(">>> postPersist");
    }

    @PreUpdate
    public void preUpdate() {
        System.out.println(">>> preUpdate");
    }

    @PostUpdate
    public void postUpdate() {
        System.out.println(">>> postUpdate");
    }

    @PreRemove
    public void preRemove() {
        System.out.println(">>> preRemove");
    }

    @PostRemove
    public void postRemove() {
        System.out.println(">>> postRemove");
    }

    @PostLoad
    public void postLoad() {
        System.out.println(">>> postLoad");
    }

    /**
     * PrePersist, PreUpdate 사용 예
     *
     *
     *     @PrePersist
     *     public void prePersist() {
     *         this.createdAt = LocalDateTime.now();
     *         this.updatedAt = LocalDateTime.now();
     *     }
     *
     *     @PreUpdate
     *     public void preUpdate() {
     *         this.updatedAt = LocalDateTime.now();
     *     }
     *
     *
     */

}
