class Solution {
    public String destCity(List<List<String>> paths) {
        HashSet <String> seen=new HashSet<>();
        for(List<String> path:paths){
            seen.add(path.get(0));
        }
        for (List<String> path:paths){
            if(!seen.contains(path.get(1))){
                return path.get(1);
            }
        }
        return "";
    }
}