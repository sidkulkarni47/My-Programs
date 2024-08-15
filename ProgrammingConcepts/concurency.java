class MyThread extends Thread {
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println(i);
        }
    }
}

public class concurency {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start();
    }
}
