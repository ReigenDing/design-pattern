package main

import "fmt"

type department interface {
	excute(*patient)
	setNext(department)
}

type reception struct {
	next department
}

func (r *reception) excute(p *patient) {
	if p.registerationDone {
		fmt.Println("Patient registration already done")
		r.next.excute(p)
		return
	}
	fmt.Println("Reception registering patient")
	p.registerationDone = true
	r.next.excute(p)
}

func (r *reception) setNext(next department) {
	r.next = next
}

type doctor struct {
	next department
}

func (d *doctor) excute(p *patient) {
	if p.doctorCheckUpdateDone {
		fmt.Println("Doctor checkup already done")
		d.next.excute(p)
		return
	}
	fmt.Println("Doctor checking patient")
	p.doctorCheckUpdateDone = true
	d.next.excute(p)
}

func (d *doctor) setNext(next department) {
	d.next = next
}

type medical struct {
	next department
}

func (m *medical) excute(p *patient) {
	if p.medicineDone {
		fmt.Println("Medicine already given to patient")
		m.next.excute(p)
		return
	}
	fmt.Println("Medical giving medicine patient")
	p.medicineDone = true
	m.next.excute(p)
}

func (m *medical) setNext(next department) {
	m.next = next
}

type cashier struct {
	next department
}

func (c *cashier) excute(p *patient) {
	if p.paymentDone {
		fmt.Println("Payment done")
		c.next.excute(p)
		return
	}
	fmt.Println("Cashier getting money from patient")
}

func (c *cashier) setNext(next department) {
	c.next = next
}

type patient struct {
	name                  string
	registerationDone     bool
	doctorCheckUpdateDone bool
	medicineDone          bool
	paymentDone           bool
}

func main() {
	cashier := &cashier{}

	// ser next fot medical department
	medical := &medical{}
	medical.setNext(cashier)

	// Set next for doctor department
	doctor := &doctor{}
	doctor.setNext(medical)

	// Set next fot reception department
	reception := &reception{}
	reception.setNext(doctor)

	patient := &patient{name: "abc"}
	reception.excute(patient)

}
