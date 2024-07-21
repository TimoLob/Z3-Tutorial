def DeclareList(sort):
 List = Datatype('List_of_%s' % sort.name())
 List.declare('cons', ('head', sort), ('tail', List))
 List.declare('nil')
 return List.create()

IntList     = DeclareList(IntSort())
RealList    = DeclareList(RealSort())
IntListList = DeclareList(IntList)

l1 = IntList.cons(10, IntList.nil)
l2 = RealList.cons("1/3", RealList.nil)
