//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.Arrays;
//
//public class Main {
//    static int N;
//    static String[] charList;
//    static int[] numCheck = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
//    static int[] numList;
//    static boolean isFirst = false;
//    static String minNum;
//    static String maxNum;
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        N = Integer.parseInt(br.readLine());
//        numList = new int[N+1];
//        charList = br.readLine().split(" ");
//
//        func(0);
//        System.out.println(maxNum);
//        System.out.println(minNum);
//    }
//
//    public static void func(int idx) {
//        if(idx > N) {
//            if (!isFirst) {
//                minNum = Arrays.toString(numList).replaceAll("[^0-9]","");
//                isFirst = true;
//            }
//            maxNum = Arrays.toString(numList).replaceAll("[^0-9]","");
//            return;
//        }
//
//        for (int i = 0; i < 10; i++) {
//            if (numCheck[i] == -1) {
//                if(idx == 0) {
//                    numList[idx] = i;
//                    numCheck[i] = idx;
//                    func(idx + 1);
//                    numList[idx] = 0;
//                    numCheck[i] = -1;
//                }
//                else {
//                    if (isCorrect(numList[idx-1], i, charList[idx-1])) {
//                        numList[idx] = i;
//                        numCheck[i] = idx;
//                        func(idx + 1);
//                        numList[idx] = 0;
//                        numCheck[i] = -1;
//                    }
//                }
//            }
//        }
//    }
//
//    public static boolean isCorrect(int num1, int num2, String op) {
//        if(op.equals("<")) {
//            return num1 < num2;
//        }
//        else {
//            return num1 > num2;
//        }
//    }
//}
