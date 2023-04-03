
def lastElement[A](list: List[A]): A = {
  list.last
}

def secondLastElement[A](list: List[A]): A = {
  list.init.last
}



@main def mainProg: Unit = {
  val LastResult = lastElement(List(1, 1, 2, 3, 5, 8))
  val SecondLastResult = secondLastElement(List(1, 1, 2, 3, 5, 8))

  println(LastResult)
  println(SecondLastResult)

}
