List<int[]> array = new ArrayList();
array.add(new int[]{1,2,3});
List<Integer> list = Arrays.asList(1,3,5,7);
List<Integer> quare = list.stream().map(x->x*x).collect(Collecter.toList());
