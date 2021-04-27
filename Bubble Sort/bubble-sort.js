function bubbleSort(array) {
	var temp;

	for (var i = 0; i < array.length; i++) {
		for (var j = i; j < array.length; j++) {
			if (array[i] > array[j]) {
				// swap
				temp = array[i];
				array[i] = array[j];
				array[j] = temp;
			}
		}
	}
}

var array = [];

for (var i = 0; i < 100; i++) {
	// Get random number from 1 to 100
	var randomNumber = Math.floor((Math.random() * 100) + 1);
	array.push(randomNumber);
}

console.log(array);

bubbleSort(array);

console.log(array);
