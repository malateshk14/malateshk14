let m1 = new Map();
m1.set("k1", "v1");
console.log(m1.get(m1.get("k1")))

if(m1.has("k1")){
    console.log("map has key k1");
}

let size = m1.size;

// Although map[key] also works, e.g. we can set map[key] = 
m1["k2"] = "v2";

//--------custom object as keys
let obj1 = {"john": 1};
m1.set(obj1, "some value for obj1 key");
console.log(m1.get(obj1))// some value for obj1 key
let obj2 = {"john": 1};
console.log(m1.get(obj2))//undefined

/*
map.keys() – returns an iterable for keys,
map.values() – returns an iterable for values,
map.entries() – returns an iterable for entries [key, value], it’s used by default in for..of.
*/

for(let key of m1.keys()){
    console.log("key ->", key)
}
