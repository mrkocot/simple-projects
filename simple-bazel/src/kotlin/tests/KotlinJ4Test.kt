package tests

import io.kotest.common.runBlocking
import io.kotest.matchers.ints.shouldBeExactly
import io.kotest.matchers.nulls.shouldBeNull
import kotlinx.coroutines.delay
import org.junit.Test

class KotlinJ4Test {
    @Test
    fun doSomething() {
        val twoPlusOne = 2 + 1
        val three = 3
        twoPlusOne shouldBeExactly three
    }

    @Test
    fun `test with multiple words`() {
        val nothing = emptyList<String>().firstOrNull()
        nothing.shouldBeNull()
    }

    @Test
    fun wrongTest() {
        throw ArithmeticException()
        2 + 2 shouldBeExactly 5
    }

    @Test
    fun longTest() {
        runBlocking { delay(3_700) }
        2 + 2 shouldBeExactly 4
    }
}
