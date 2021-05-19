function selectionSort(array) {
	var temp;

	for (var i = 0; i < array.length; i++) {
		var smallestIndex = i;
		for (var j = i; j < array.length; j++) {
			if (array[smallestIndex] > array[j]) {
				smallestIndex = j;
			}
		}

		// swap current i & smallest index
		temp = array[smallestIndex];
		array[smallestIndex] = array[i];
		array[i] = temp;
	}

	return array;
}

let array = [];

dataLength = 100

for (var i = 0; i < dataLength; i++) {
	// Get random number from 1 to dataLength
	var randomNumber = i;
	array.push(randomNumber);
}

// shuffle array
array = array.sort(() => Math.random() - 0.5)

console.log(array);
var startTime = new Date();

sortedArray = selectionSort(array);

endTime = new Date();

var timeDiff = endTime - startTime; //in ms
console.log(timeDiff + "ms sorting time.");
// strip the ms
timeDiff /= 1000;

// get seconds 
var seconds = Math.round(timeDiff);
console.log(seconds + " seconds elapsed.")

console.log(sortedArray);
