package main

import (
	"fmt"
	"strings"
)

func updateEmailStandartFormat(s string) string {
	var items = strings.Split(s, "@")
	var localName, domainNamwe string = items[0], items[1]
	localName = strings.Replace(localName, ".", "", -1)
	var indexPlus int = strings.Index(localName, "+")
	if indexPlus != -1 {
		localName = localName[:indexPlus]
	}
	var email string = localName + "@" + domainNamwe
	return email
}

func numUniqueEmails(emails []string) int {
	info := make(map[string]bool)
	res := 0
	for i := 0; i < len(emails); i++ {
		emailUpdate := updateEmailStandartFormat(emails[i])
		_, flag := info[emailUpdate]
		if !flag {
			res++
		}
		info[emailUpdate] = true
	}

	return res
}

func main() {
	var emails = []string{"test.e.mail+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"}

	res := numUniqueEmails(
		emails,
	)

	fmt.Println(res)
}
