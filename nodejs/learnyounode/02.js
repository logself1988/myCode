//console.log(process.argv);

var i=2,sum=0;

while (i < process.argv.length){
	sum=sum+Number(process.argv[i]);
	i++;
}

console.log(sum);
