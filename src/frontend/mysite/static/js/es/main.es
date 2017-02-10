function swap(x, y) {
    if (x != y) {
        var old = x;
        let tmp = x;
        x = y;
        y = tmp;
    }

    console.log(typeof(old));   // number
    console.log(typeof(tmp));   // undefined
}
