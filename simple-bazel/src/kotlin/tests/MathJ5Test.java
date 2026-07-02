package tests;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class MathJ5Test {
  @DisplayName("Add test")
  @Test
  public void addTest() {
    assertEquals(4, 2 + 2);
  }

  @Nested
  class AdditionalTests {
    @Nested
    class More {
      @DisplayName("Subtract test")
      @Test
      public void subtractTest() {
        assertEquals(1, 3 - 2);
      }
    }

    @DisplayName("Multiply test")
    @Test
    public void multiplyTest() {
      assertEquals(28, 4 * 7);
    }
  }

  @DisplayName("Wrong test")
  @Test
  public void wrongTest() {
    assertEquals(4, 0);
  }

  @Disabled
  @DisplayName("Disabled test")
  @Test
  public void disabledTest() {
    assertEquals(555, 111);
  }
}
