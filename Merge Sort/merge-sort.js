function mergeSort(array) {
	if (array.length == 1) {
		return array;
	}

	var middle = Math.floor(array.length / 2);

	var leftArray = array.slice(0, middle);
	var rightArray = array.slice(middle, array.length);

	var sortedLeft = mergeSort(leftArray);
	var sortedRight = mergeSort(rightArray);

	var leftPointer = 0;
	var rightPointer = 0;

	let tempList = [];
	while (leftPointer < sortedLeft.length && rightPointer < sortedRight.length) {
		left = sortedLeft[leftPointer];
		right = sortedRight[rightPointer];

		if (left > right) {
			tempList.push(right);
			rightPointer += 1;
		}
		else {
			tempList.push(left);
			leftPointer += 1;
		}
	}

	while (leftPointer < sortedLeft.length) {
		tempList.push(sortedLeft[leftPointer]);
		leftPointer += 1;
	}

	while (rightPointer < sortedRight.length) {
		tempList.push(sortedRight[rightPointer]);
		rightPointer += 1;
	}

	return tempList;
}

let array = [];

dataLength = 10000000

for (var i = 0; i < dataLength; i++) {
	// Get random number from 1 to dataLength
	var randomNumber = i;
	array.push(randomNumber);
}

// shuffle array
array = array.sort(() => Math.random() - 0.5)

console.log(array);
var startTime = new Date();

sortedArray = mergeSort(array);

endTime = new Date();

var timeDiff = endTime - startTime; //in ms
console.log(timeDiff + "ms sorting time.");
// strip the ms
timeDiff /= 1000;

// get seconds 
var seconds = Math.round(timeDiff);
console.log(seconds + " seconds elapsed.")

console.log(sortedArray);
