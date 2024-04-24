import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        TreeSet<Integer> ts = new TreeSet<>();

        int n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            String[] cmds = br.readLine().split(" ");
            String cmd = cmds[0];
            switch(cmd){
                case "add":
                    ts.add(Integer.parseInt(cmds[1]));
                    break;
                case "remove":
                    ts.remove(Integer.parseInt(cmds[1]));
                    break;
                case "find":
                    boolean isContain = ts.contains(Integer.parseInt(cmds[1]));
                    if(isContain){
                        bw.write("true" + "\n");
                    }else{
                        bw.write("false" + "\n");
                    }
                    break;
                case "lower_bound":
                    Integer vlb = ts.ceiling(Integer.parseInt(cmds[1]));
                    if(vlb == null){
                        bw.write("None" + "\n");
                    }else{
                        bw.write(Integer.toString(vlb) + "\n");
                    }
                    break;
                case "upper_bound":
                    Integer vub = ts.higher(Integer.parseInt(cmds[1]));
                    if(vub == null){
                        bw.write("None" + "\n");
                    }else{
                        bw.write(Integer.toString(vub) + "\n");
                    }
                    break;
                case "largest":
                    if(ts.size() == 0){
                        bw.write("None" + "\n");
                    }else{
                        int v = ts.last();
                        bw.write(Integer.toString(v) + "\n");
                    }
                    break;
                case "smallest":
                    if(ts.size() == 0){
                        bw.write("None" + "\n");
                    }else{
                        int v = ts.first();
                        bw.write(Integer.toString(v) + "\n");
                    }
                    break;
            }
            // bw.write(">>>" + "\n");
            // for(int tv : ts){
            //     bw.write(Integer.toString(tv)+ " ");
            // }
            // bw.write("\n");
        }

        bw.flush();
        bw.close();

    }
}