package tests;

import org.junit.Test;
import org.junit.Assert;

public class MathJ4Test {
  @Test
  public void addTest() {
    Assert.assertEquals(4, 2 + 2);
  }

  @Test
  public void subtractTest() {
    Assert.assertEquals(1, 3 - 2);
  }

  @Test
  public void multiplyTest() {
    Assert.assertEquals(28, 4 * 7);
  }

  @Test
  public void wrongTest() {
    Assert.assertEquals(4, 0);
  }

//    @Test
//    public void waitTest() {
//        try {
//            Thread.sleep(5000);
//        } catch (InterruptedException e) {
//            throw new RuntimeException(e);
//        }
//    }
}
