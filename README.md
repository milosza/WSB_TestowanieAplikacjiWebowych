# WSB_TestowanieAplikacjiWebowych
Repozytoriom kursu WSB Testowanie Aplikacji Webowych (semestr 4, zima 2019)

Zadanie 1: Utworzenie przypadków testowych

Zadania 2: Unittest
Przypadek testowy:
Rejestracja nowego użytkownika na stronie wizzair.com używając adresu email - dane niepoprawne (niekompletny email)
Oczekiwany rezultat:
Przycisk "zarejestruj się" jest nieaktywny. 
Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny


Zadanie 3: Behavior-driven development (BDD)
Feature: Log in to poczta on wp.pl
Scenario Outline: Log in to poczta

Given: I am on the Poczta tab of wp.pl
When: I log in by using <login> and <password>
Then: I <is logged in> logged in in to poczta

Examples:
| login | password | is logged in |
| wsb_bdd | stxnext_bdd | am |
| milena@user.com | test | am not |
