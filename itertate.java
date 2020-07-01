import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class itertate {
    public static void main(String [] args){
        Map<Integer,String> foo = new HashMap<>();
        int[] array = {1,2,3,4,5,6,7,8,9};
        for(int i=0;i<array.length;i++){
            foo.put(array[i],"");
        }
        for(Map.Entry m : foo.entrySet()){    
            System.out.println(m.getKey()+":"+m.getValue());    
        }
        List<String> list = new ArrayList<String>(); 
  
        list.add("A"); 
        list.add("B"); 
        list.add("C"); 
        list.add("D"); 
        list.add("E"); 
  
        // Iterator to traverse the list 
        Iterator iterator = list.iterator(); 
  
        System.out.println("List elements : "); 
  
        while (iterator.hasNext()) 
            System.out.print(iterator.next() + " "); 
  
        System.out.println();  
        
    }
}