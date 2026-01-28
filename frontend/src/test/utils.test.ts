import { describe, it, expect, beforeEach, afterEach } from 'vitest'

describe('Utility Functions', () => {
  describe('LocalStorage Token Management', () => {
    beforeEach(() => {
      localStorage.clear()
    })

    afterEach(() => {
      localStorage.clear()
    })

    it('should store and retrieve token from localStorage', () => {
      const token = 'test-token-123'
      localStorage.setItem('token', token)
      
      const retrieved = localStorage.getItem('token')
      expect(retrieved).toBe(token)
    })

    it('should remove token from localStorage', () => {
      localStorage.setItem('token', 'test-token')
      localStorage.removeItem('token')
      
      const retrieved = localStorage.getItem('token')
      expect(retrieved).toBeNull()
    })

    it('should return null for non-existent token', () => {
      const retrieved = localStorage.getItem('token')
      expect(retrieved).toBeNull()
    })
  })

  describe('String Validation', () => {
    it('should validate email format', () => {
      const validEmail = 'test@example.com'
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      
      expect(emailRegex.test(validEmail)).toBe(true)
    })

    it('should reject invalid email format', () => {
      const invalidEmail = 'not-an-email'
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      
      expect(emailRegex.test(invalidEmail)).toBe(false)
    })

    it('should validate non-empty strings', () => {
      const nonEmpty = 'test'
      const empty = ''
      
      expect(nonEmpty.trim().length).toBeGreaterThan(0)
      expect(empty.trim().length).toBe(0)
    })
  })

  describe('Array Operations', () => {
    it('should filter array items', () => {
      const items = [1, 2, 3, 4, 5]
      const filtered = items.filter(item => item > 3)
      
      expect(filtered).toEqual([4, 5])
      expect(filtered.length).toBe(2)
    })

    it('should map array items', () => {
      const items = [1, 2, 3]
      const mapped = items.map(item => item * 2)
      
      expect(mapped).toEqual([2, 4, 6])
    })

    it('should handle empty arrays', () => {
      const empty: number[] = []
      const filtered = empty.filter(item => item > 0)
      
      expect(filtered).toEqual([])
      expect(filtered.length).toBe(0)
    })
  })
})
