<?hh

class MyA<+Tco, -Tcontra, Tinv> {}

class MyB<-T1, T2> extends MyA<Sub, T1, T2> {}

class MyC<+T1, T2> extends MyA<T1, Super, T2> {}

class Super {}

class Sub {}

function takes_my_a(MyA<Sub, Super, Super> $_): void {}

function subtype_bad_contravariant(MyB<Sub, Super> $x): void {
  takes_my_a($x);
}

function subtype_bad_invariant(MyB<Super, Sub> $x): void {
  takes_my_a($x);
}

function subtype_bad_covariant(MyC<Super, Super> $x): void {
  takes_my_a($x);
}
