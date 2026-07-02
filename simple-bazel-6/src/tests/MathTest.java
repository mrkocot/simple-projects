package src.tests;

import org.junit.Test;
import org.junit.Assert;
import org.junit.rules.TestName;

public class MathTest {
//  @DisplayName("Add test")
  @Test
  public void addTest() {
    Assert.assertEquals(4, 2 + 2);
  }

//  @DisplayName("Subtract test")
  @Test
  public void subtractTest() {
    Assert.assertEquals(1, 3 - 2);
  }

//  @DisplayName("Multiply test")
  @Test
  public void multiplyTest() {
    Assert.assertEquals(28, 4 * 7);
  }

//  @DisplayName("Wrong test")
  @Test
  public void wrongTest() {
    Assert.assertEquals(4, 0);
  }
}
