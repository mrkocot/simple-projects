package numberer;

public class LargeNumberPrinter {
  public static void main(String[] args) throws InterruptedException {
    for (int i = 0; i < 1670; i += 167) {
      System.out.println(i);
      Thread.sleep(1000);
      if (i == 501) {
        try {
          throwInterrupt();
        } catch (ArithmeticException ae) {
          ae.printStackTrace(System.out);
        }
      }
    }
  }

  private static void throwInterrupt() throws ArithmeticException {
    throw new ArithmeticException("Exception for test purposes");
  }
}
