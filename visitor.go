package main

import "fmt"

type shape interface {
	getType() string
	accept(visitor)
}

type square struct {
	side int
}

func (s *square) accept(v visitor) {
	v.visitForSquare(s)
}

func (s *square) getType() string {
	return "Square"
}

type circle struct {
	radius int
}

func (c *circle) accept(v visitor) {
	v.visitForCircle(c)
}
func (c *circle) getType() string {
	return "Circle"
}

type rectangle struct {
	l int
	b int
}

func (t *rectangle) accept(v visitor) {
	v.visitForRectangle(t)
}

func (t *rectangle) getType() string {
	return "Rectangle"
}

type visitor interface {
	visitForSquare(*square)
	visitForCircle(*circle)
	visitForRectangle(*rectangle)
}

type areaCaculator struct {
	area int
}

func (a *areaCaculator) visitForSquare(s *square) {
	fmt.Printf("Calculating area for square side => %d\n", s.side)
}

func (a *areaCaculator) visitForCircle(c *circle) {
	fmt.Printf("Calculating area for circle radius => %d\n", c.radius)

}

func (a *areaCaculator) visitForRectangle(r *rectangle) {

	fmt.Printf("Calculating area for rectangle b => %d l => %d\n", r.b, r.l)
}

type middleCoordinates struct {
	x int
	y int
}

func (m *middleCoordinates) visitForSquare(s *square) {
	fmt.Printf("Calculating middle point coordinate for square side => %d\n", s.side)

}

func (m *middleCoordinates) visitForCircle(c *circle) {
	fmt.Printf("Calculating middle point coordinate for circle radius => %d\n", c.radius)
}
func (m *middleCoordinates) visitForRectangle(r *rectangle) {
	fmt.Printf("Calculating middle point coordinate for recrange b => %d, l => %d", r.b, r.l)
}

func main() {
	square := &square{side: 2}
	circle := &circle{radius: 3}
	rectangle := &rectangle{l: 2, b: 3}

	areaCaculator := &areaCaculator{}

	square.accept(areaCaculator)
	circle.accept(areaCaculator)
	rectangle.accept(areaCaculator)

	fmt.Println()

	middleCoordinates := &middleCoordinates{}

	square.accept(middleCoordinates)
	circle.accept(middleCoordinates)
	rectangle.accept(middleCoordinates)

}
