import java.util.Scanner;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // n과 m을 입력받음
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        scanner.nextLine(); // 숫자 입력 후 개행문자 처리

        // n개의 숫자를 TreeSet에 저장
        TreeSet<Integer> numbers = new TreeSet<>();
        for (int i = 0; i < n; i++) {
            numbers.add(scanner.nextInt());
        }
        scanner.nextLine(); // 숫자 입력 후 개행문자 처리

        // m개의 숫자에 대해 처리
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int query = scanner.nextInt();
            // TreeSet에서 query 이상의 가장 작은 요소를 찾음
            Integer result = numbers.ceiling(query);
            if (result == null) {
                output.append("-1\n");
            } else {
                output.append(result).append("\n");
            }
        }
        scanner.close();

        // 결과 출력
        System.out.print(output.toString());
    }
}