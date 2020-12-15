package main

import (
	//"math/big"
	"fmt"
	"github.com/fentec-project/gofe/data"
	"github.com/fentec-project/gofe/quadratic"
	"math/big"
)


func main() {

	//Retrieve polX, polY and D from data directory
	x, _ := readVectFromFile("data/poly_X.txt")
	y, _ := readVectFromFile("data/poly_Y.txt")
	F, _ := readMatFromFile("data/D.txt")

	fmt.Println(x)
	fmt.Println(y)
	fmt.Println(F)

	bound := big.NewInt(100000) // Upper bound for coordinates of vectors x, y, and matrix F
	dec := SGPSimulator(x, y, F, bound)
	fmt.Println(dec)

	quadDec := QuadSimulator(x, y, bound, F)
	fmt.Println(quadDec)

}

//
func QuadSimulator(x data.Vector, y data.Vector, bound *big.Int, F data.Matrix) bool {
	quad, _ := quadratic.NewQuad(len(x), len(y), bound)
	quadPubKey, quadSecKey, _ := quad.GenerateKeys()
	cipher, _ := quad.Encrypt(x, y, quadPubKey)
	key, _ := quad.DeriveKey(quadSecKey, F)
	quadDec, _ := quad.Decrypt(cipher, key, F)

	if quadDec.BitLen() == 0{
		return true
	}
	return false
}

//
func SGPSimulator(x, y data.Vector, F data.Matrix, bound *big.Int) bool {
	l := len(x) // length of input vectors
	//fmt.Println(l)
	sgp := quadratic.NewSGP(l, bound)     // Create scheme instance
	msk, _ := sgp.GenerateMasterKey()     // Create master secret key
	cipher, _ := sgp.Encrypt(x, y, msk)   // Encrypt input vectors x, y with secret key
	key, _ := sgp.DeriveKey(msk, F)       // Derive FE key for decryption
	dec, _ := sgp.Decrypt(cipher, key, F) // Decrypt the result to obtain x^T * F * y

	if dec.BitLen() == 0{
		return true
	}
	return false
}
