/**
 * Created by janeluck on 8/14/16.
 */

function fib(max) {
    var n = 0, a = 0, b = 1;
    while (n < max) {
        console.log(b);
        a = b;
        b = a + b;
        n++
    }
}

